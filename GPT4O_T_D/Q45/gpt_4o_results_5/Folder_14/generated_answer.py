from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substr = s[4:6].lower()
    letters = [ch for ch in substr if ch.isalpha()]

    def can_form_palindrome(chars):
        odd_count = sum((1 for count in chars.values() if count % 2 != 0))
        return odd_count <= 1
    perms = set()

    def generate_palindromes(chars, current_half):
        if len(current_half) == len(chars) // 2:
            odd_char = [char for char, count in chars.items() if count % 2 != 0]
            center = odd_char[0] if odd_char else ''
            palindrome = current_half + center + current_half[::-1]
            if len(palindrome) >= 3:
                perms.add(palindrome)
            return
        for char in set(chars):
            if chars[char] >= 2:
                chars[char] -= 2
                generate_palindromes(chars, current_half + char)
                chars[char] += 2
    letter_counts = Counter(letters)
    if can_form_palindrome(letter_counts):
        generate_palindromes(letter_counts, '')
    return perms