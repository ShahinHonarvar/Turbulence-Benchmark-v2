def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[125:284]
    for i in range(109, 127):
        for j in range(0, len(substring) - i + 1):
            sub_str = substring[j:j + i]
            if all((c.isalpha() for c in sub_str)) and sub_str.lower() == sub_str.lower()[::-1]:
                result.add(sub_str)
    return result