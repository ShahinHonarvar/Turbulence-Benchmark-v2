def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(4, 10):
        substring = s[i].lower()
        if substring in english_letters:
            for j in range(i - 1, 3, -1):
                substring = s[j].lower() + substring
                if substring in english_letters:
                    for k in range(i + 1, 10):
                        substring = substring + s[k].lower()
                        if len(substring) >= 7 and substring == substring[::-1]:
                            palindromes.add(substring)
    return palindromes