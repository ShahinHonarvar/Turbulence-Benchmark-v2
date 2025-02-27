import string

def palindromes_between_indices(input_str):
    sub_str = input_str[3:8].lower()
    letters = ''
    for char in sub_str:
        if char in string.ascii_letters:
            letters += char
    letters_arr = list(letters)
    length = len(letters_arr)
    palindromes = set()
    if length >= 3:
        first = 0
        second = length - 1
        while second >= 0:
            while first <= second:
                second_half_arr = list(reversed(letters_arr[first:second + 1]))
                second_half = ''.join(second_half_arr)
                if second_half == letters_arr[first:second + 1] and len(second_half) >= 6:
                    palindromes.add(second_half)
                first += 1
            second -= 1
            first = 0
    return palindromes