def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:7] if char.isalpha()]
    palindrome_set = set()

    def generate_palindromes(current_letters):
        if len(current_letters) >= 7:
            current_letters.sort()
            while True:
                palindrome = ''.join(current_letters)
                if palindrome == palindrome[::-1]:
                    palindrome_set.add(palindrome)
                if not next_permutation(current_letters):
                    break

    def next_permutation(arr):
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i < 0:
            return False
        j = len(arr) - 1
        while j > i and arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = (arr[j], arr[i])
        arr[i + 1:] = sorted(arr[i + 1:])
        return True
    generate_palindromes(letters)
    return palindrome_set