def palindromes_of_specific_lengths(string):
    result = set()
    for idx in range(30, 85):
        for length in range(12, 21):
            left, right = (idx - length // 2, idx + length // 2 + 1)
            if left >= 0 and left <= len(string) and (right >= 0) and (right <= len(string)) and (string[left:right].lower() == string[left:right][::-1].lower()):
                result.add(string[left:right])
    return result