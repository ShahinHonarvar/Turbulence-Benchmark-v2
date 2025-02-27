def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_str = s[5:10].lower()
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 4, len(sub_str) + 1):
            if sub_str[i:j] == sub_str[i:j][::-1] and all((c in english_letters for c in sub_str[i:j])):
                palindromes.add(sub_str[i:j])
    return palindromes