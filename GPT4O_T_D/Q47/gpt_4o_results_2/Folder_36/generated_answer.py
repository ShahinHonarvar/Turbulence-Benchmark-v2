def palindromes_of_specific_lengths(s):
    substring = s[124:284]
    result = set()
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            segment = substring[start:start + length]
            cleaned_segment = ''.join(filter(str.isalpha, segment)).lower()
            if cleaned_segment == cleaned_segment[::-1]:
                result.add(segment)
    return result