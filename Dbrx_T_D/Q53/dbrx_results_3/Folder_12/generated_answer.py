def palindrome_of_length_at_least_n(string, n=51):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    return {palindrome for i in range(len(string) - n + 1) for palindrome in (string[i:i + n],) if palindrome == palindrome[::-1]}