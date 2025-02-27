def palindromes_between_indices(s):
    chars = ''.join([ch for ch in s if ch.isalpha() and 2 <= s.index(ch) <= 7])
    length, palindromes = (len(chars), set())
    for i in range(length):
        for j in range(i + 5, length):
            word = chars[i:j + 1]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes