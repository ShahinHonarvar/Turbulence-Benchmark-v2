def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    lower_s = s[1:8].lower()
    if set(lower_s).issubset(english_letters):
        for i in range(len(lower_s)):
            for j in range(i + 3, len(lower_s) + 1):
                substr = lower_s[i:j]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes