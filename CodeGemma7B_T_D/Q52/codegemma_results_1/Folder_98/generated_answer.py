def palindrome_of_length_n(s):
    f = s.lower()
    vowels = set('aeiouAEIOU')
    res = {'', ''}
    for letter in f:
        if letter not in vowels:
            res.add(letter * 6)
    return set({word for word in res if len(word) == 6})