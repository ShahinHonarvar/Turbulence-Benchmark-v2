def palindromes_of_specific_lengths(s):
    s = s[1:10]
    result = set()
    for length in range(3, 8):
        for i in range(len(s) - length + 1):
            word = s[i:i + length]
            if word.lower() == word[::-1].lower():
                result.add(word)
    return result