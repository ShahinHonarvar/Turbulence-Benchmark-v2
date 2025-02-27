def palindromes_between_indices(s):

    def can_form_palindrome(char_freq):
        odd_count = sum((1 for count in char_freq.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(half, center):
        if len(half) == total_length // 2:
            palindrome = half + center + half[::-1]
            palindromes.add(palindrome)
            return
        for char in char_count:
            if char_count[char] > 0:
                char_count[char] -= 2
                generate_palindromes(half + char, center)
                char_count[char] += 2
    s = s.lower()
    relevant_chars = ''.join([c for c in s[4:7] if c.isalpha()])
    char_count = {char: relevant_chars.count(char) for char in set(relevant_chars)}
    palindromes = set()
    if not can_form_palindrome(char_count):
        return palindromes
    for length in range(3, len(relevant_chars) + 1):
        total_length = length
        half_count = {char: count // 2 for char, count in char_count.items()}
        for char in char_count:
            if char_count[char] % 2 != 0:
                generate_palindromes('', char)
                break
        else:
            generate_palindromes('', '')
    return palindromes