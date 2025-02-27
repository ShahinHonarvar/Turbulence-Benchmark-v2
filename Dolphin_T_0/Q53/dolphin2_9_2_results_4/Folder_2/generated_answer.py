def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 55
    palindrome_set = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if ''.join(reversed(substring)) == substring:
            palindrome_set.add(substring)
    return palindrome_set