def palindromes_between_indices(s):
    letters = s[5:8].lower()
    length = len(letters)
    result = set()

    def is_palindrome(sub_str):
        return sub_str == sub_str[::-1]

    def generate_permutations(sub_str, length):
        if length == 1:
            if is_palindrome(sub_str):
                result.add(sub_str)
        else:
            for perm in permutations(sub_str, length - 1):
                s = ''.join(perm)
                if s not in result:
                    generate_permutations(s + sub_str[-1], length)
    if length >= 4:
        generate_permutations(letters, length)
    return result