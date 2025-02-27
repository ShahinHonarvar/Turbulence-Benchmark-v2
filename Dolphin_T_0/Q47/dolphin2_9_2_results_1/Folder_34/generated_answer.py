def palindromes_of_specific_lengths(s):
    substring = s[200:301]
    result = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            if all(('a' <= substring[i + j] <= 'z' for j in range(length))):
                word = substring[i:i + length]
                if word.lower() == word.lower()[::-1]:
                    result.add(word)
    return result