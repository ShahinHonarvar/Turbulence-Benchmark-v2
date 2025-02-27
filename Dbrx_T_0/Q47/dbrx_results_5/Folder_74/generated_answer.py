def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(30, 85):
        for length in range(12, 21):
            if i + length <= 85 and s[i:i + length].lower() == s[i:i + length][::-1].lower():
                palindromes.add(s[i:i + length])
    return palindromes