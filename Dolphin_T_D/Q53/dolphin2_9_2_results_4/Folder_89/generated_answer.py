def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_palindromes = set()
    for length in range(43, len(s) + 1):
        for i in range(0, len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                set_palindromes.add(s[i:i + length])
    return set_palindromes