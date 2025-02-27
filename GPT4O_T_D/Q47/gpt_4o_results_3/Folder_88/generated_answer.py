def palindromes_of_specific_lengths(s):
    result = set()
    substring = ''.join(filter(str.isalpha, s[11:88])).lower()
    for i in range(len(substring)):
        for length in range(4, 6):
            if i + length <= len(substring):
                segment = substring[i:i + length]
                if segment == segment[::-1]:
                    result.add(segment)
    return result