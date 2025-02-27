def palindromes_between_indices(s):
    sub_str = s[3:5].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_str = ''.join(filter(lambda x: x in english_letters, sub_str))
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 3, len(sub_str) + 1):
            palindromes.add(sub_str[i:j][::-1] + sub_str[i:j])
    return palindromes