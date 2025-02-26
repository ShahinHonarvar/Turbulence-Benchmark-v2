def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:8] if char.isalpha()]
    result = set()

    def generate_palindromes(current_chars, remaining_chars):
        if len(current_chars) >= 5 and len(current_chars) % 2 == 1:
            mid = len(current_chars) // 2
            palindrome = current_chars[:mid] + current_chars[mid] + current_chars[mid - 1::-1]
            result.add(palindrome)
        for i in range(len(remaining_chars)):
            new_chars = current_chars + [remaining_chars[i]]
            new_remaining = remaining_chars[:i] + remaining_chars[i + 1:]
            generate_palindromes(new_chars, new_remaining)
    generate_palindromes([], letters)
    return result