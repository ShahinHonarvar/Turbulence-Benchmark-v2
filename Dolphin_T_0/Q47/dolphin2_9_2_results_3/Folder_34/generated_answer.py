def palindromes_of_specific_lengths(s):
    substring = s[200:301]
    result_set = set()
    for length in range(10, 51):
        substring = ''.join([ch for ch in substring if ch.isalpha()])
        for i in range(0, len(substring)):
            word = substring[i:i + length]
            if len(word) == length and word.lower() == word.lower()[::-1]:
                result_set.add(word)
    return result_set