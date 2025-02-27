def palindromes_of_specific_lengths(s):
    s = s[11:84]
    result = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 13, min(length, start + 67)):
            substring = s[start:end + 1]
            filtered = ''.join(filter(str.isalpha, substring)).lower()
            if filtered == filtered[::-1]:
                result.add(filtered)
    return result