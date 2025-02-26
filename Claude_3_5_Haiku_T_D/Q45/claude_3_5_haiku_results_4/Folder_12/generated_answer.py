def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:9] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current_letters, used_indices):
        if len(current_letters) >= 4 and len(current_letters) % 2 == 0:
            current_letters.sort()
            mid = len(current_letters) // 2
            left_half = current_letters[:mid]
            right_half = current_letters[mid:][::-1]
            if left_half == right_half:
                palindrome = ''.join(current_letters)
                palindromes.add(palindrome)
        for i in range(len(letters)):
            if i not in used_indices:
                current_letters.append(letters[i])
                generate_palindromes(current_letters, used_indices + [i])
                current_letters.pop()
    generate_palindromes([], [])
    return palindromes