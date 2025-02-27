from functools import cmp_to_key

def return_n_smallest_chars(chars: str) -> list:

    def compare(left, right):
        left_ascii = ord(left)
        right_ascii = ord(right)
        return left_ascii - right_ascii
    sorted_chars = sorted(list(chars), key=cmp_to_key(compare))
    return sorted_chars[:37]