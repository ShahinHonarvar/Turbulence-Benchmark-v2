def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    s_lower = s[3:10].lower()
    for i in range(len(s_lower)):
        if s_lower[i] in english_letters:
            for j in range(i + 1, len(s_lower)):
                if s_lower[j] in english_letters:
                    temp = s_lower[i:j + 1]
                    if temp == temp[::-1] and len(temp) >= 7:
                        palindromes.add(temp)
    return palindromes