def palindrome_of_length_at_least_n(string, n=24):
    string = ''.join((e.lower() for e in string if e.isalpha()))
    return {palindrome for palindrome in {string[i:j] for i in range(len(string)) for j in range(i + n, len(string) + 1)} if palindrome == palindrome[::-1]}