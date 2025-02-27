def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(136, 152):
        for i in range(106, 281):
            if i + length - 1 <= 280:
                sub = s[i:i + length].lower()
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub)
    return palindromes