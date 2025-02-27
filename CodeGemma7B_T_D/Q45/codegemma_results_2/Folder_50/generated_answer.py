import itertools

def palindromes_between_indices(x):
    nums = list(range(4, 9))
    english = 'abcdefghijklmnopqrstuvwxyz'
    result = set()
    for k in itertools.product(nums, repeat=5):
        front = ''.join([english[i] for i in k])
        back = front[::-1]
        if front in x.lower() and back in x.lower():
            if len(front) >= 5:
                result.add(front)
    return result