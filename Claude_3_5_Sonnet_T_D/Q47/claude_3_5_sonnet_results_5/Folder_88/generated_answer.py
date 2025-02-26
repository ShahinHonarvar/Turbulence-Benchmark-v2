def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:88]
    lowercase_substring = substring.lower()
    for i in range(len(lowercase_substring)):
        for length in range(4, 6):
            if i + length <= len(lowercase_substring):
                candidate = lowercase_substring[i:i + length]
                if candidate == candidate[::-1] and candidate.isalpha():
                    result.add(substring[i:i + length])
    return result