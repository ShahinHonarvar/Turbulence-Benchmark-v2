def palindromes_of_specific_lengths(s):
    filtered_substring = ''.join(filter(str.isalpha, s[101:293]))
    filtered_substring = filtered_substring.lower()
    n = len(filtered_substring)
    result = set()
    for start in range(n):
        for end in range(start + 153, min(n, start + 182)):
            substring = filtered_substring[start:end + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result