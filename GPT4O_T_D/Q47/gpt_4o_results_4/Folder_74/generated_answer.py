def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(30, 85):
        for length in range(12, 21):
            if i + length <= 85:
                substring = s[i:i + length]
                filtered = ''.join(filter(str.isalpha, substring)).lower()
                if filtered == filtered[::-1] and len(filtered) == length:
                    palindromes.add(substring)
    return palindromes