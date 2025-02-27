def palindromes_of_specific_lengths(s):
    substring = s[10:100]
    palindrome_set = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((ch.isalpha() for ch in sub)):
                if sub.lower() == sub[::-1].lower():
                    palindrome_set.add(sub)
    return palindrome_set