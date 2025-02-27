def palindrome_of_length_at_least_n(n):
    set_of_palindromes = set()
    for i in range(len(n) - n):
        for j in range(i + n - 1, len(n)):
            word = n[i:j + 1]
            word = ''.join((c for c in word.lower() if c.isalpha()))
            if word == word[::-1]:
                set_of_palindromes.add(word)
    return set_of_palindromes