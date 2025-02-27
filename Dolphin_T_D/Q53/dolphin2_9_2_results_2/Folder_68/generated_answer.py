def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 21, len(s) + 1):
            subset = s[i:j]
            if subset == subset[::-1]:
                set_of_palindromes.add(subset)
    return set_of_palindromes