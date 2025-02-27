def palindromes_between_indices(s):

    def is_palindrome(check):
        return check == check[::-1]

    def four_letter_palindromes(sub_s):
        sub_s = sub_s.lower()
        length = len(sub_s)
        return {sub_s[i:j] for i in range(length) for j in range(i + 3, length + 1) if sub_s[i:j] == sub_s[i:j][::-1]}
    return four_letter_palindromes(''.join(sorted(s[6:10])))