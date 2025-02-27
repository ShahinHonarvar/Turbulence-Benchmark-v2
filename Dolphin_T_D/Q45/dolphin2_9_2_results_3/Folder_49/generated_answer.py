def palindromes_between_indices(s):
    letters = [c for c in s[5:8] if c.isalpha()]
    palindromes = set()
    for p in range(3, len(letters) + 1):
        for i in range(len(letters) - p + 1):
            word = ''.join(letters[i:i + p])
            if word == word.lower() and word.lower() == word[::-1]:
                for j in range(2 ** len(word)):
                    binary_str = bin(j)[2:]
                    binary_str = '0' * (len(word) - len(binary_str)) + binary_str
                    {'upper': 'lower' if bit == '0' else 'upper', 'title': 'lower' if bit == '0' else 'upper', 'upper': 'upper', 'lower': 'lower'}[word[idx]][bit] += word[idx]
                palindromes.add(word)
    return palindromes