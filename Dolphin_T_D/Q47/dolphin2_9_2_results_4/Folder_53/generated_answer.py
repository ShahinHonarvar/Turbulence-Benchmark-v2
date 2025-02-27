def palindromes_of_specific_lengths(s):
    s = s[1:300]
    palindromes = set()
    for length in range(3, 11):
        for i in range(len(s) - length + 1):
            if len(set(s[i:i + length].lower()) & set('abcdefghijklmnopqrstuvwxyz')) == len(s[i:i + length]):
                if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                    palindromes.add(s[i:i + length])
    return palindromes