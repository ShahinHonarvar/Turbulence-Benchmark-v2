def palindromes_between_indices(s):

    def can_form_palindrome(freq_map):
        odd_count = sum((1 for count in freq_map.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(half, middle):
        if len(half) == 0:
            yield middle
            return
        for i, char in enumerate(half):
            if i > 0 and half[i] == half[i - 1]:
                continue
            next_half = half[:i] + half[i + 1:]
            for rest in generate_palindromes(next_half, middle):
                yield (char + rest + char)
    substring = s[3:7].lower()
    filtered_chars = [ch for ch in substring if ch.isalpha()]
    char_frequency = {}
    for ch in filtered_chars:
        char_frequency[ch] = char_frequency.get(ch, 0) + 1
    if not can_form_palindrome(char_frequency):
        return set()
    half = []
    middle = ''
    for char, count in char_frequency.items():
        half.extend(char * (count // 2))
        if count % 2 == 1:
            middle = char
    half.sort()
    palindromes_set = set()
    for pal_half in generate_palindromes(half, middle):
        if len(pal_half) >= 3:
            palindromes_set.add(pal_half)
    return palindromes_set