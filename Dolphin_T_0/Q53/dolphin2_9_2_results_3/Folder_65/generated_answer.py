def palindrome_of_length_at_least_n(word):
    word = word.lower()
    n = 15
    palindromes = set()
    for i in range(len(word) - n + 1):
        for j in range(i + n, len(word) + 1):
            sub = word[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes