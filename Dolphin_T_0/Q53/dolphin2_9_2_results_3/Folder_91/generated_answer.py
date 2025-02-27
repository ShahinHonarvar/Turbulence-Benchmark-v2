def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for length in range(7, len(s) + 1):
        for i in range(len(s) - length + 1):
            word = s[i:i + length]
            if word == word[::-1]:
                set_of_palindromes.add(word)
    return set_of_palindromes