def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:97]
    for i in range(len(substring)):
        for j in range(i + 45, min(i + 53, len(substring) + 1)):
            substring_slice = substring[i:j]
            if substring_slice.isalpha():
                if substring_slice.lower() == substring_slice.lower()[::-1]:
                    result.add(substring_slice)
    return result