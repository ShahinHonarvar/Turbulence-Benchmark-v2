def palindromes_between_indices(s):
    palindromes = set()
    substring = s[4:6]
    for letter in substring:
        if letter.isalpha():
            for i in range(5):
                for j in range(i + 2, 6):
                    sub = substring[i:j]
                    sub = sub.lower()
                    if sub == sub[::-1]:
                        palindromes.add(sub)
    return palindromes