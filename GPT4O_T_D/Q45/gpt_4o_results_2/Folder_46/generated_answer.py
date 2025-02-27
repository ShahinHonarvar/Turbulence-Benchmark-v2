def palindromes_between_indices(s):

    def can_form_palindrome(letters_count):
        odd_count = sum((1 for count in letters_count.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(half_str, middle_char, length, path, result):
        if len(path) == len(half_str):
            palindrome = path + middle_char + path[::-1] if middle_char else path + path[::-1]
            if len(palindrome) >= length:
                result.add(palindrome)
            return
        for char in sorted(set(half_str)):
            new_half_str = half_str.replace(char, '', 1)
            generate_palindromes(new_half_str, middle_char, length, path + char, result)
    if len(s) < 10:
        return set()
    sub_str = s[4:10].lower()
    letters_count = {}
    for char in sub_str:
        if char.isalpha():
            letters_count[char] = letters_count.get(char, 0) + 1
    if not can_form_palindrome(letters_count):
        return set()
    half_part = ''
    middle_char = ''
    for char, count in letters_count.items():
        half_part += char * (count // 2)
        if count % 2 != 0:
            middle_char = char
    result = set()
    generate_palindromes(half_part, middle_char, 6, '', result)
    return result