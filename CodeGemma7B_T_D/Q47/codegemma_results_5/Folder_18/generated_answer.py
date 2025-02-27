def palindromes_of_specific_lengths(word):
    result = set()
    for i in range(11, 84):
        for length in range(13, 67):
            low = i - length // 2
            high = i + length // 2 - (1 if length % 2 != 0 else 0)
            if low >= 0 and high <= len(word) - 1 and (word[low:high + 1].lower() == word[low:high + 1][::-1].lower()):
                result.add(word[low:high + 1])
    return result