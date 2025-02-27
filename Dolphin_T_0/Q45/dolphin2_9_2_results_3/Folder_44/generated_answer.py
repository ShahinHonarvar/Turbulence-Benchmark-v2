def palindromes_between_indices(s):
    letter_freq = [0 for _ in range(26)]
    for c in s[2:8]:
        if 'a' <= c.lower() <= 'z':
            letter_freq[ord(c.lower()) - ord('a')] += 1
    palindromes = set()
    for len_ in range(3, 9):
        for perm in permutations(letter_freq, len_):
            word = ''.join([chr(i + ord('a')) * freq for i, freq in enumerate(perm)])
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes