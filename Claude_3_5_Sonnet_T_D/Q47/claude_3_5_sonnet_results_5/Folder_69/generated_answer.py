def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:97]
    lowercase_substring = substring.lower()
    for i in range(len(substring)):
        for length in range(45, 53):
            if i + length <= len(substring):
                candidate = lowercase_substring[i:i + length]
                if candidate == candidate[::-1] and candidate.isalpha():
                    result.add(substring[i:i + length])
    return result