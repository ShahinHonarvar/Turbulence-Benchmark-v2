def palindromes_of_specific_lengths(s):
    substring = s[127:288]
    palindromes = set()
    for length in range(119, 142):
        for start_index in range(0, len(substring) - length + 1):
            text = substring[start_index:start_index + length]
            if text.lower() == text.lower()[::-1] and text.isalpha():
                palindromes.add(text)
    return palindromes