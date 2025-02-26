def palindromes_of_specific_lengths(s):
    substring = s[24:98]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 37, len(substring) + 1)):
            slice = substring[i:j]
            if slice.isalpha() and slice.lower() == slice.lower()[::-1]:
                result.add(slice)
    return result