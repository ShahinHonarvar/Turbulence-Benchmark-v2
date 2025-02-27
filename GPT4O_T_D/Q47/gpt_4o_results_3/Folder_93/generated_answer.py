def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[17:96]
    for start in range(len(substring)):
        for end in range(start + 13, min(len(substring), start + 50)):
            candidate = substring[start:end + 1]
            filtered_candidate = ''.join(filter(str.isalpha, candidate)).lower()
            if filtered_candidate == filtered_candidate[::-1]:
                result.add(candidate)
    return result