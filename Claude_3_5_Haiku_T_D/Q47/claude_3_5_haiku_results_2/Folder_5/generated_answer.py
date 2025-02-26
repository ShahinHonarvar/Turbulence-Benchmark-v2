def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[63:71].lower()
    for i in range(len(substring)):
        for j in range(i + 3, i + 6):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate == candidate[::-1] and candidate.isalpha():
                    result.add(candidate)
    return result