def palindromes_between_indices(s):
    sub_str = s[2:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_str = ''.join((ch for ch in sub_str if ch in english_letters))
    arrangements = set()
    for i in range(len(filtered_str)):
        for j in range(i + 1, len(filtered_str) + 1):
            arrangements.add(filtered_str[i:j])
    palindromes = set((word for word in arrangements if word == word[::-1] and len(word) >= 6))
    return palindromes