def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    for length in range(72, len(s) + 1):
        for i in range(len(s) - length + 1):
            sSection = s[i:i + length]
            if sSection == sSection[::-1]:
                result_set.add(sSection)
    return result_set